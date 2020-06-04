<?php
  require "pdo_conn.php";

  $numb = $_POST['numb'];

  $stmt = $pdo_conn->prepare("SELECT userId, userEmail, products_json, orderNumb, orderDate
, buyer, orderState, productsPrice, saleDiscount, billedPoint
, deliveryCharge, finalBill, paymentMethod, depositor, accountNumb
, payDay, receiverName, receiverAddress, receiverCallNumb, receiverCellphone
, createdDate, deliveryState, deliveryNumb FROM all_orders WHERE numb = $numb");
  $stmt->execute();
  $all = $stmt->fetchAll(PDO::FETCH_ASSOC);
  $json_all = json_encode($all,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
  header('Content-Type: application/json; charset=utf8');
  echo urldecode($json_all);

  // serId, userEmail, products_json, orderNumb, orderDate
// , buyer, orderState, productsPrice, saleDiscount, billedPoint
// , deliveryCharge, finalBill, paymentMethod, depositor, accountNumb
// , payDay, receiverName, receiverAddress, receiverCallNumb, receiverCellphone
// , createdDate



 ?>
