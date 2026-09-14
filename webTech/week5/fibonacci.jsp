<%@ page language="java" contentType="text/html; charset=UTF-8" %>

<html>
<head>
    <title>Fibonacci Series</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background-color: lightblue;
        }

        h2 {
            color: darkblue;
        }
    </style>
</head>

<body>
    <h2>Fibonacci Series</h2>

    <%
        int n = 10;
        int a = 0, b = 1;

        for (int i = 0; i < n; i++) {
            out.print(a + " ");

            int c = a + b;
            a = b;
            b = c;
        }
    %>

</body>
</html>
