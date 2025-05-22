import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/jdbc")
public class JdbcServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String param = request.getParameter("userInput"); // Getting input from URL or POST body

        // Database connection details (hardcoded for demonstration purposes)
        String jdbcUrl = "jdbc:mysql://localhost:3306/demo";
        String jdbcUser = "root";
        String jdbcPass = "password";

        Connection conn = null;
        Statement stmt = null;
        try {
            // Establishing connection
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection(jdbcUrl, jdbcUser, jdbcPass);

            // Crafting an SQL query (vulnerable to SQL Injection)
            String sql = "SELECT * FROM users WHERE username = '" + param + "'";

            stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);

            // Output the result
            out.println("<html><body>");
            while (rs.next()) {
                out.println("User: " + rs.getString("username") + "<br>");
            }
            out.println("</body></html>");

        } catch (Exception e) {
            out.println("Error: " + e.getMessage());
        } finally {
            try {
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            } catch (Exception e) {
                // Handle errors during cleanup
            }
        }
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response); // Reuse the POST handling logic
    }
}