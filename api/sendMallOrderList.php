<?php
// error_reporting(E_ALL);
// ini_set("display_errors", 1);

  require "pdo_conn.php";

  $json_mallOrderList = $_POST['json_mallOrderList'];

  // json화된 mallOrderList 가 오면
  $mallOrderList = json_decode($json_mallOrderList,true);
  // json을 다시 array로 만든다.

  error_log(date("Y-m-d H:i:s")
  ."\n".$json_mallOrderList."\n"
  , 3, "/var/www/html/phplog.log");
  //
  error_log(date("Y-m-d H:i:s")
  ."\n".count($mallOrderList)."\n"
  , 3, "/var/www/html/phplog.log");
  // $mallListCount = count($mallOrderList);

  for ($i=0; $i < count($mallOrderList); $i++) {
    //count($mallOrderList)
    $get_mall_id = $mallOrderList[$i]['mall_id'];
    $get_mall_order = $mallOrderList[$i]['mall_order'];
    // $get_mall_id = "3";
    // $get_mall_order = "3";

    // $query = "UPDATE mall_order_list SET
    //           mall_order = :mall_order WHERE mall_id = :mall_id ";
    // $stmt = $pdo_conn->prepare($query);
    // $stmt->bindParam(':mall_order',$get_mall_order, PDO::PARAM_INT);
    // $stmt->bindParam(':mall_id',$get_mall_id, PDO::PARAM_INT);

    $query = "UPDATE mall_order_list SET mall_order = ? WHERE mall_id = ? ";
    $stmt = $pdo_conn->prepare($query);
    $stmt->bindParam(1,$get_mall_order);
    $stmt->bindParam(2,$get_mall_id);
    $stmt->execute();
    // error_log(date("Y-m-d H:i:s")
    // ."\n"."넣기 성공"."\n"
    // , 3, "/var/www/html/phplog.log");
    // code...
  }



  //
  // $stmt = $pdo_conn->prepare("INSERT INTO mall_order_list (mall_id, mall_name, mall_order, createdDate) VALUES (?,?,?,NOW())");
  // $stmt->bindParam(1,$
  // row 하나하나씩 excute를 해줘야한다.

  // array에는 수정된 쇼핑몰 순서가 순서대로 담겨있고
  // 그럼 array의 index의 순서대로 서버 db - mall_order_list table 에 저장한다.
  // 엄밀히 말하면 update이다.
  // 그리고 아무값도 echo 하지 않는다.
  // (그럼 클라이언트에서 response 코드를 받아서 200이면 잘된것, 400,500이면 잘안된것으로 인지할 수 있을것이다.)
 ?>
