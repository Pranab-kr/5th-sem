<!DOCTYPE html>
<html>
<head>
    <title>Odd or Even</title>
</head>

<body>
    <h2>Check Odd or Even</h2>

    <form method="post">
        Enter a number:
        <input type="number" name="num" required>
        <br><br>

        <input type="submit" value="Check">
    </form>

    <%
        String n = request.getParameter("num");

        if (n != null && !n.isEmpty()) {
            int num = Integer.parseInt(n);

            if (num % 2 == 0) {
    %>
                <h3><%= num %> is Even</h3>
    <%
            } else {
    %>
                <h3><%= num %> is Odd</h3>
    <%
            }
        }
    %>

</body>
</html>
