<?php

// error_reporting(E_ALL);
// ini_set("display_errors", 1);

  try {
    $pdo = "mysql:host=13.209.50.185;port=3306;dbname=choi;charset=utf8";
    $pdo_conn = new PDO($pdo, "wonwoo", "cww1003");
    $pdo_conn->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
    $pdo_conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // $strProdNumbArray = $_GET["prodNumbArray"];
    // $strMallNameArray = $_GET["mallNameArray"];
    $strProdNumbArray = $_POST["prodNumbArray"];
    $strMallNameArray = $_POST["mallNameArray"];
    //  $_POST 로 하니까 값을 못받아 오더니
    // echo $strProdNumbArray."<br>";
    // echo $strMallNameArray."<br>";
    //
    $prodNumbArray = explode(',', $strProdNumbArray);
    $mallNameArray = explode(',', $strMallNameArray);

    // $prodNumb = "7286b0000";
    // $mallName = "allProducts_vintagesister";
    $array=array();

      // $prodNumb = $prodNumbArray[1];
      // echo $prodNumb."<br>";
      // $mallName = "allProducts_".$mallNameArray[1];
      // echo $mallName."<br>";
      //
      // $query = "SELECT prodNumb, mallName FROM $mallName WHERE prodNumb=?";
      // echo $query."<br>";
      // $stmt = $pdo_conn->prepare($query);
      // // $stmt->bindParam(1,$mallName);
      // $stmt->bindParam(1,$prodNumb);
      // $stmt->execute();
      // $row = $stmt->fetch(PDO::FETCH_ASSOC);
      // print_r($row);
      //



    $i = 0;
    while (count($prodNumbArray)-1 > $i) {
      $prodNumb = $prodNumbArray[$i];
      $mallName = "allProducts_".$mallNameArray[$i];

      $query = "SELECT prodNumb, mallName FROM $mallName WHERE prodNumb=?";
      $stmt = $pdo_conn->prepare($query);
      // $stmt->bindParam(1,$mallName);
      $stmt->bindParam(1,$prodNumb);
      $stmt->execute();
      $row = $stmt->fetchAll(PDO::FETCH_ASSOC);
      if (count($row)==0) {
        // echo "아무것도 없다";
        // 여기서 없다는 값을 넣어주면 되겠다.\
        $row['prodNumb']="x";
        $row['mallName']='x';
        array_push($array, $row);
        // code...
      }else {
        $row2['prodNumb']=$row[0]['prodNumb'];
        $row2['mallName']=$row[0]['mallName'];
        array_push($array, $row2);

      }


      // print_r($row);
    // echo "sdfsdfsdfsdf";
    // echo "string";
      $i++;
    }
    $json_all = json_encode($array, JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
    header('Content-Type: application/json; charset=utf8');                 // 이 해더가 있음으로 해서 json을 보여주기 쉬운형태로 화면에 표시된다.
    echo urldecode($json_all);
    error_log(date("Y-m-d H:i:s")."\n".$json_all."\n", 3, "/var/www/html/phplog.log");



  } catch (PDOException $e) {
      echo $e->getMessage();
      echo "실패";
      error_log(date("Y-m-d H:i:s")."\n".$e."\n", 3, "/var/www/html/phplog.log");

  }


 ?>
