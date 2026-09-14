<!DOCTYPE html>
<html>
<head>
    <title>Greatest of Three Numbers</title>
</head>

<body>
    <h2>Find Greatest of Three Numbers</h2>

    <form method="post">
        Enter first number:
        <input type="number" name="num1" required>
        <br><br>

        Enter second number:
        <input type="number" name="num2" required>
        <br><br>

        Enter third number:
        <input type="number" name="num3" required>
        <br><br>

        <input type="submit" value="Find Greatest">
    </form>

    <%
        String n1 = request.getParameter("num1");
        String n2 = request.getParameter("num2");
        String n3 = request.getParameter("num3");

        if (n1 != null && n2 != null && n3 != null) {
            int num1 = Integer.parseInt(n1);
            int num2 = Integer.parseInt(n2);
            int num3 = Integer.parseInt(n3);

            int greatest;

            if (num1 >= num2 && num1 >= num3) {
                greatest = num1;
            } else if (num2 >= num1 && num2 >= num3) {
                greatest = num2;
            } else {
                greatest = num3;
            }
    %>

        <h3>First Number: <%= num1 %></h3>
        <h3>Second Number: <%= num2 %></h3>
        <h3>Third Number: <%= num3 %></h3>
        <h3>Greatest Number: <%= greatest %></h3>

    <%
        }
    %>

</body>
</html>
