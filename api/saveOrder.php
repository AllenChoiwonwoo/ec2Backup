<?php
require 'pdo_conn.php';

$userId = $_POST['userId'];
$userEmail = $_POST['userEmail'];
$products_json = $_POST['products_json'];
$orderNumb = $_POST['orderNumb'];
$orderDate = $_POST['orderDate'];
$buyer = $_POST['buyer'];
$orderState = $_POST['orderState'];
$productsPrice = $_POST['productsPrice'];
$saleDiscount = $_POST['saleDiscount'];
$billedPoint = $_POST['billedPoint'];
$deliveryCharge = $_POST['deliveryCharge'];
$finalBill = $_POST['finalBill'];
$paymentMethod = $_POST['paymentMethod'];
$depositor = $_POST['depositor'];
$accountNumb = $_POST['accountNumb'];
$payDay = $_POST['payDay'];
$receiverName = $_POST['receiverName'];
$receiverAddress = $_POST['receiverAddress'];
$receiverCallNumb = $_POST['receiverCallNumb'];
$receiverCellphone = $_POST['receiverCellphone'];


$stmt = $pdo_conn->prepare("INSERT INTO all_orders (
                  userId, userEmail, products_json, orderNumb, orderDate
                , buyer, orderState, productsPrice, saleDiscount, billedPoint
                , deliveryCharge, finalBill, paymentMethod, depositor, accountNumb
                , payDay, receiverName, receiverAddress, receiverCallNumb, receiverCellphone
                , createdDate ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NOW() ) ");
$stmt->bindParam(1,$userId);
$stmt->bindParam(2,$userEmail);
$stmt->bindParam(3,$products_json);
$stmt->bindParam(4,$orderNumb);
$stmt->bindParam(5,$orderDate);
$stmt->bindParam(6,$buyer);
$stmt->bindParam(7,$orderState);
$stmt->bindParam(8,$productsPrice);
$stmt->bindParam(9,$saleDiscount);
$stmt->bindParam(10,$billedPoint);
$stmt->bindParam(11,$deliveryCharge);
$stmt->bindParam(12,$finalBill);
$stmt->bindParam(13,$paymentMethod);
$stmt->bindParam(14,$depositor);
$stmt->bindParam(15,$accountNumb);
$stmt->bindParam(16,$payDay);
$stmt->bindParam(17,$receiverName);
$stmt->bindParam(18,$receiverAddress);
$stmt->bindParam(19,$receiverCallNumb);
$stmt->bindParam(20,$receiverCellphone);

$stmt->execute();

error_log(date("Y-m-d H:i:s")
."\n"."saveOrder 에서 db에 주문내역 저장완료"."\n"
, 3, "/var/www/html/phplog.log");

 ?>
