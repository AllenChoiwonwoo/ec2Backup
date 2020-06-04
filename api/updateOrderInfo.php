<?php
  // error_reporting(E_ALL);
  // ini_set("display_errors", 1);

  require "pdo_conn.php";
  // echo "string";



    $orderNumb = $_POST['orderNumb'];
    // $orderNumb = "2019070915-1000";
    $chagedOrderState = $_POST['changedOrderState'];
    // $chagedOrderState = "미결제";

    $query = "UPDATE all_orders SET orderState = ? WHERE orderNumb = ? ";
    $stmt = $pdo_conn->prepare($query);
    $stmt->bindParam(1,$chagedOrderState);
    // $stmt->bindParam(1,"2019070915-1000");
    $stmt->bindParam(2,$orderNumb);
    // $stmt->bindParam(2,"미결제");
    $stmt->execute();



 ?>
