<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mining Animation</title>
    <style>
        body {
            margin: 0;
            background-color: #0d2745;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
        .circle {
            width: 150px;
            height: 150px;
            border: 10px solid rgba(255, 255, 255, 0.2);
            border-top: 10px solid #0088cc;
            border-radius: 50%;
            animation: spin 2s linear infinite;
        }
        .logo {
            position: absolute;
            width: 70px;
            height: 70px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="circle">
        <img src="ton.png" class="logo" alt="TON Logo">
    </div>
</body>
</html>
