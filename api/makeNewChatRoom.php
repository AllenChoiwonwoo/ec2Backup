<?php
    require "pdo_conn.php";

    $newRoomData_json = $_GET['newRoomData_json'];
    // $newRoomData_json = '{"roomName":"hithere","roomTages":"#hihi#tetete","roomCertains_email":"dkssudnjsdn@naver.com","roomCertains_userId":3,"maxUserVolume":3,"createdDate":"2019-27-09"}';
    // print($newRoomData_json);
    // error_log(date("Y-m-d H:i:s")
    // ."\n".$newRoomData_json."\n"
    // , 3, "/var/www/html/phplog.log");

    $newRoomData = json_decode($newRoomData_json,true);
    // error_log(date("Y-m-d H:i:s")
    // ."\n".$newRoomData."\n"
    // , 3, "/var/www/html/phplog.log");

    $roomName = $newRoomData['roomName'];
    // print($roomName);
    // error_log(date("Y-m-d H:i:s")
    // ."\n".$roomName
    // , 3, "/var/www/html/phplog.log");
    $roomTages = $newRoomData['roomTages'];
    // print($roomTages);
    // error_log(date("Y-m-d H:i:s")
    // ."\n".$roomTages
    // , 3, "/var/www/html/phplog.log");
    $roomCertains_email = $newRoomData['roomCertains_email'];
    // error_log(date("Y-m-d H:i:s")
    // ."\n".$roomCertains_email
    // , 3, "/var/www/html/phplog.log");
    $roomCertains_userId = $newRoomData['roomCertains_userId'];
    // error_log(date("Y-m-d H:i:s")
    // ."\n".$roomCertains_userId
    // , 3, "/var/www/html/phplog.log");
    $maxUserVolume = $newRoomData['maxUserVolume'];
    // error_log(date("Y-m-d H:i:s")
    // ."\n".$maxUserVolume
    // , 3, "/var/www/html/phplog.log");
    $createdDate = $newRoomData['createdDate'];
    // error_log(date("Y-m-d H:i:s")
    // ."\n".$createdDate
    // , 3, "/var/www/html/phplog.log");
    //
    error_log(date("Y-m-d H:i:s")
    ."\n".$roomName."\n".$roomTages."\n".$roomCertains_email."\n".$roomCertains_userId."\n".$maxUserVolume."\n".$createdDate."\n"
    , 3, "/var/www/html/phplog.log");
    //
    $query = "INSERT INTO chatting_rooms
    (roomName, roomTages, roomCertainsId, roomCertainsEmail, maxUserVolume)
    VALUES (?, ?, ?, ?, ? )";
    $stmt = $pdo_conn->prepare($query);
    $stmt->bindParam(1,$roomName);
    $stmt->bindParam(2,$roomTages);
    $stmt->bindParam(3,$roomCertains_userId);
    $stmt->bindParam(4,$roomCertains_email);
    $stmt->bindParam(5,$maxUserVolume);
    $stmt->execute();





 ?>
