package conexionsql;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Conexionsql {
    
    public static void main(String[] args) {
        Connection conn = null;
        final String url = "jdbc:mysql://localhost:3306/";
        final String dbName = "PROYECTO_GESTION";
        final String userName = "root";
        final String password = "";

        try {
            conn = DriverManager.getConnection(url + dbName, userName, password);
            if (!conn.isClosed()) {
                System.out.println("CONEXION BD...");

                // Inserción de registros en tablas secundarias
                PreparedStatement stmt = conn.prepareStatement("INSERT INTO TIPO_CLIENTE (TipCliCod, TipCliNom, TipCliEstReg) VALUES (?, ?, 'A')");
                stmt.setInt(1, 1);
                stmt.setString(2, "Persona juridica");
                stmt.executeUpdate();
                stmt.close();

                stmt = conn.prepareStatement("INSERT INTO ESTADO_CLIENTE (EstCliCod, EstCliNom, EstCliEstReg) VALUES (?, ?, 'A')");
                stmt.setInt(1, 1);
                stmt.setString(2, "Cesado");
                stmt.executeUpdate();
                stmt.close();

                stmt = conn.prepareStatement("INSERT INTO ESTADO_REGISTRO (EstRegCod, EstRegNom, EstRegEstReg) VALUES (?, ?, 'A')");
                stmt.setInt(1, 1);
                stmt.setString(2, "Activo");
                stmt.executeUpdate();
                stmt.close();

                // Inserción de registros en tablas principales
                stmt = conn.prepareStatement("INSERT INTO CLIENTE (CliCod, CliNom, CliFecIng, TipCliCod, EstCliCod, EstRegCod) VALUES (?, ?, ?, ?, ?, ?)");
                stmt.setInt(1, 1);
                stmt.setString(2, "Julio");
                stmt.setDate(3, java.sql.Date.valueOf("2023-06-09"));
                stmt.setInt(4, 1);
                stmt.setInt(5, 1);
                stmt.setInt(6, 1);
                stmt.executeUpdate();
                stmt.close();

                // Consulta de registros
                stmt = conn.prepareStatement("SELECT * FROM CLIENTE WHERE CliCod = ?");
                stmt.setInt(1, 1);
                ResultSet rs = stmt.executeQuery();
                while (rs.next()) {
                    System.out.println("CliCod: " + rs.getInt("CliCod"));
                    System.out.println("CliNom: " + rs.getString("CliNom"));
                    System.out.println("CliFecIng: " + rs.getDate("CliFecIng"));
                    System.out.println("TipCliCod: " + rs.getInt("TipCliCod"));
                    System.out.println("EstCliCod: " + rs.getInt("EstCliCod"));
                    System.out.println("EstRegCod: " + rs.getInt("EstRegCod"));
                    System.out.println();
                }
                rs.close();
                stmt.close();
/*
                // Actualización de registros
                stmt = conn.prepareStatement("UPDATE CLIENTE SET CliNom = ? WHERE CliCod = ?");
                stmt.setString(1, "Alvaro");
                stmt.setInt(2, 1);
                stmt.executeUpdate();
                stmt.close();

                // Borrado de registros
                stmt = conn.prepareStatement("DELETE FROM CLIENTE WHERE CliCod = ?");
                stmt.setInt(1, 1);
                stmt.executeUpdate();
                stmt.close();

                // Borrado de registros en tablas secundarias
                stmt = conn.prepareStatement("DELETE FROM TIPO_CLIENTE WHERE TipCliCod = ?");
                stmt.setInt(1, 1);
                stmt.executeUpdate();
                stmt.close();

                stmt = conn.prepareStatement("DELETE FROM ESTADO_CLIENTE WHERE EstCliCod = ?");
                stmt.setInt(1, 1);
                stmt.executeUpdate();
                stmt.close();

                stmt = conn.prepareStatement("DELETE FROM ESTADO_REGISTRO WHERE EstRegCod = ?");
                stmt.setInt(1, 1);
                stmt.executeUpdate();
                stmt.close();
*/
            }
        } catch (Exception e) {
            System.err.println("Exception: " + e.getMessage());
        } finally {
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException e) {
                System.err.println("SQLException: " + e.getMessage());
            }
        }
    }
}
