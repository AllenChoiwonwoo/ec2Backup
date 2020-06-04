<?php
/*
  단어정의 :
    상품업데이트 = 쇼핑몰의 신상품 업데이트
  목적 :
    앱에서 사용자가 '소핑몰'탭을 눌렀을 시
    화면에 쇼핑몰별 상품 업데이트 정보를 보여줘야한다.
    (ex :
        A 쇼핑몰. 60개 업데이트, 2019-05-31
        C 쇼핑몰. 50개 업데이트, 2019-05-29
        D 쇼핑몰. 90개 업데이트, 2019-05-20
        .
        .
    )
    그러기 위하여 DB에 저장된 쇼핑몰의 상품업데이트 정보를 가져와 클라이언트에게 보내줘야한다.



*/

  require 'pdo_conn.php';

  $mallNumb = 1; //빈티지 톡 은 1번
  $array = array();

  // 쇼핑몰 번호,이름,mallUrl, newProdDate, newProdCount, createddate
  // $query = "select mallNumb, mallName, mallUrl, newProdDate, newProdCount, createddate FROM mallUpdateRecord WHERE mallNumb=? ORDER BY newProdDate DESC LIMIT 1";

  $query = "SELECT mallNumb, mallName, mallUrl, newProdDate, newProdCount, createddate
  FROM mallUpdateRecord WHERE mallNumb=$mallNumb ORDER BY newProdDate DESC LIMIT 1";
   //

  // $query = "SELECT mallNumb, mallName, mallUrl, newProdDate, newProdCount, createddate
  // FROM mallUpdateRecord WHERE mallNumb=(select mallNumb from mallUpdateRecord) ORDER BY newProdDate DESC LIMIT 1";

  $stmt = $pdo_conn->prepare($query);
  // $stmt->bindParm(1, $mallNumb);

  $stmt->execute();
  $result1 = $stmt->fetch(PDO::FETCH_ASSOC);
  // print_r($result1);
  array_push($array, $result1);
  // $array[0] = $result1;
  // echo "______________________________________________";

/** 이거까지 더하면 2개 보냄 */
  $query = "SELECT mallNumb, mallName, mallUrl, newProdDate, newProdCount, createddate
  FROM mallUpdateRecord WHERE mallNumb=2 ORDER BY newProdDate DESC LIMIT 1";

  $stmt = $pdo_conn->prepare($query);
  // $stmt->bindParm(1, $mallNumb);

  $stmt->execute();
  $result2 = $stmt->fetch(PDO::FETCH_ASSOC);
  // print_r($result2);
  array_push($array, $result2);
  // $array[1] = $result2;

  // echo "______________________________________________";

  $query = "SELECT mallNumb, mallName, mallUrl, newProdDate, newProdCount, createddate
  FROM mallUpdateRecord WHERE mallNumb=3 ORDER BY newProdDate DESC LIMIT 1";

  $stmt = $pdo_conn->prepare($query);
  // $stmt->bindParm(1, $mallNumb);

  $stmt->execute();
  $result3 = $stmt->fetch(PDO::FETCH_ASSOC);
  // print_r($result3);
  array_push($array, $result3);
  // $array[2] = $result3;

  // echo "______________________________________________";
  // $json_all = json_encode($result ,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
  $json_all = json_encode($array ,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
  header('Content-Type: application/json; charset=utf8');
  echo urldecode($json_all);


 ?>
