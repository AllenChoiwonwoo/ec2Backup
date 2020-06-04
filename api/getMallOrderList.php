<?php
  require "pdo_conn.php";

  // $json_mallOrderList = $_POST['json_mallOrderList'];
  //
  // // json화된 mallOrderList 가 오면
  // $mallOrderList = json_decode($json_mallOrderList,true);
  // json을 다시 array로 만든다.
  // $ShowAndHideClassifier = $_GET['ShowAndHideClassifier'];

  $stmt = $pdo_conn->prepare("SELECT mall_id, mall_name, kor_name, mall_order FROM mall_order_list WHERE mall_order > 0 ORDER BY mall_order");
  $stmt->execute();
  $all = $stmt->fetchAll(PDO::FETCH_ASSOC);
  $json_all = json_encode($all,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
  header('Content-Type: application/json; charset=utf8');
  echo urldecode($json_all);

  // $stmt->bindParam(1,$
  // row 하나하나씩 excute를 해줘야한다.

  // array에는 수정된 쇼핑몰 순서가 순서대로 담겨있고
  // 그럼 array의 index의 순서대로 서버 db - mall_order_list table 에 저장한다.
  // 엄밀히 말하면 update이다.
  // 그리고 아무값도 echo 하지 않는다.
  // (그럼 클라이언트에서 response 코드를 받아서 200이면 잘된것, 400,500이면 잘안된것으로 인지할 수 있을것이다.)
 ?>
