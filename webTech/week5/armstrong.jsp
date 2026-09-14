<%@ page language="java" contentType="text/html; charset=UTF-8" %>

<!DOCTYPE html>
<html>
<head>
    <title>Armstrong Number</title>
</head>

<body>

    <h2>Check Armstrong Number</h2>

    <%
        int num = 153;
        int original = num;
        int sum = 0;
        int remainder;

        while (num != 0) {
            remainder = num % 10;
            sum = sum + (remainder * remainder * remainder);
            num = num / 10;
        }

        if (sum == original) {
    %>

        <h3><%= original %> is an Armstrong Number</h3>

    <%
        } else {
    %>

        <h3><%= original %> is not an Armstrong Number</h3>

    <%
        }
    %>

</body>
</html>
