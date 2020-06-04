<?php
try {
  $pdo = "mysql:host=13.209.50.185;port=3306;dbname=choi;charset=utf8";
  $pdo_conn = new PDO($pdo, "wonwoo", "cww1003");
  $pdo_conn->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
  $pdo_conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  // $a = 'tset1';
  // $b = '#test1';
  // $c = 3;
  // $d = 'dkssudnjsdn@naver.com';
  // $e = 6;
  // $query = "INSERT INTO chatting_rooms
  // (roomName, roomTages, roomCertainsId, roomCertainsEmail, maxUserVolume)
  // VALUES (?, ?, ?, ?, ? )";
  // $stmt = $pdo_conn->prepare($query);
  // $stmt->bindParam(1,$a);
  // $stmt->bindParam(2,$b);
  // $stmt->bindParam(3,$c);
  // $stmt->bindParam(4,$d);
  // $stmt->bindParam(5,$e);
  // $stmt->execute();
  // echo "hithere";

} catch (PDOException $e) {
    echo $e->getMessage();
    echo "실패";
}



 ?>
