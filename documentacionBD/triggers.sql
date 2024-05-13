DELIMITER //
CREATE PROCEDURE realizar_deposito(IN numero_cuenta_depositar VARCHAR(16), IN monto_depositar DECIMAL(10,2))
BEGIN

    DECLARE cuenta_saldo DECIMAL(10,2);

    SELECT saldo INTO cuenta_saldo
    FROM cuenta
    WHERE numero_cuenta = numero_cuenta_depositar;

    UPDATE cuenta
    SET saldo = cuenta_saldo + monto_depositar
    WHERE numero_cuenta = numero_cuenta_depositar;

END//
DELIMITER ;







DELIMITER //

CREATE PROCEDURE realizar_retiro(IN numero_cuenta_retirar VARCHAR(16), IN monto_retirar DECIMAL(10,2))
BEGIN
    DECLARE cuenta_saldo DECIMAL(10,2);

    SELECT saldo INTO cuenta_saldo
    FROM cuenta
    WHERE numero_cuenta = numero_cuenta_retirar;

    IF cuenta_saldo >= monto_retirar THEN
        UPDATE cuenta
        SET saldo = cuenta_saldo - monto_retirar
        WHERE numero_cuenta = numero_cuenta_retirar;
    
    END IF;
END//

DELIMITER ;







DELIMITER //

CREATE PROCEDURE realizar_transaccion(IN numero_cuenta_manda VARCHAR(16),IN numero_cuenta_recibe VARCHAR(16), IN monto_transferido DECIMAL(10,2)
)
BEGIN
    DECLARE cuenta_saldo_manda DECIMAL(10,2);
    DECLARE cuenta_saldo_recibe DECIMAL(10,2);

    SELECT saldo INTO cuenta_saldo_manda
    FROM cuenta
    WHERE numero_cuenta = numero_cuenta_manda;

    SELECT saldo INTO cuenta_saldo_recibe
    FROM cuenta
    WHERE numero_cuenta = numero_cuenta_recibe;

    IF cuenta_saldo_manda >= monto_transferido THEN
        UPDATE cuenta
        SET saldo = saldo - monto_transferido
        WHERE numero_cuenta = numero_cuenta_manda;

        UPDATE cuenta
        SET saldo = saldo + monto_transferido
        WHERE numero_cuenta = numero_cuenta_recibe;

        INSERT INTO registro_transferencia (
            id_cliente_tranfiere,
            id_cliente_recibe,
            fecha_hora_transferencia,
            monto_de_tranferencia
        ) VALUES (
            (SELECT ID_CLIENTE FROM cuenta WHERE numero_cuenta = numero_cuenta_manda),
            (SELECT ID_CLIENTE FROM cuenta WHERE numero_cuenta = numero_cuenta_recibe),
            NOW(),
            monto_transferido
        );
        
    
    END IF;
END//

DELIMITER ;





DELIMITER //

CREATE OR REPLACE TRIGGER ACTUALIZACION_CUENTA
BEFORE UPDATE
ON CUENTA
FOR EACH ROW
BEGIN
    DECLARE diferencia DECIMAL(10,2);

    IF OLD.saldo <> NEW.saldo THEN
        SET diferencia = NEW.saldo - OLD.saldo;

        IF diferencia > 0 THEN
            INSERT INTO REGISTRO_DEPOSITO (ID_CLIENTE_DEPOSITO, FECHA_DEPOSITO, MONTO_DEPOSITO)
            VALUES (NEW.ID_CLIENTE, NOW(), diferencia);
        ELSE
            INSERT INTO registro_retiro (id_cliente_retira, fecha_hora_retiro, monto_de_retiro)
            VALUES (NEW.ID_CLIENTE, NOW(), -diferencia);
        END IF;
    END IF;
END;
//

DELIMITER ;






DELIMITER //

CREATE TRIGGER actualizar_saldo_despues_transferencia AFTER UPDATE ON registro_transferencia
FOR EACH ROW
BEGIN
    DECLARE cuenta_saldo_manda DECIMAL(10,2);
    DECLARE cuenta_saldo_recibe DECIMAL(10,2);

    SELECT saldo INTO cuenta_saldo_manda
    FROM cuenta
    WHERE numero_cuenta = OLD.id_cliente_tranfiere;

    SELECT saldo INTO cuenta_saldo_recibe
    FROM cuenta
    WHERE numero_cuenta = OLD.id_cliente_recibe;

    UPDATE cuenta
    SET saldo = saldo + OLD.monto_de_tranferencia - NEW.monto_de_tranferencia
    WHERE numero_cuenta = OLD.id_cliente_tranfiere;

    UPDATE cuenta
    SET saldo = saldo - OLD.monto_de_tranferencia + NEW.monto_de_tranferencia
    WHERE numero_cuenta = OLD.id_cliente_recibe;
END//

DELIMITER ;
