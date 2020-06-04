<?php
    error_reporting(E_ALL);
    ini_set('display_errors', '1');

    try {
        echo "6";
        $pdo = "mysql:host=13.209.50.185;port=3306;dbname=choi;charset=utf8";
        echo "7";
        $db = new PDO($pdo, "wonwoo", "cww1003");
        $db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // insert 문
        /*$query = "insert into test1 (name) VALUES ('류쿼리')";
        echo "8";
        $stmt = $db->prepare($query);
        echo "9";*/

        // $query = "select name from ?";
        // $stmt = $db->prepare($query);
        // $stmt->execute('test1');
        // while($row=$stmt->fetch()){
        //     echo $row['name'];
        //     echo "<br>";
        // }

        // $db = null;
        // $query="insert into new_product (name ,mall_name, data, created_date) values (?, ?, ?, NOW())";
        // $st = $db->$query;
        // $st->execute('고양잉');

        $keyword = "원우몰";
        $data = "zkjdkmocijdlksfasdascv";

        $query="insert into new_product (mall_name, data, created_date) values (?, ?, NOW())";
        $st = $db->prepare($query);
        $st->bindParam(1, $keyword, PDO::PARAM_STR);
        $st->bindParam(2, $data, PDO::PARAM_STR);
        $st->execute();


        // $stmt->execute();
         echo "성공";

    } catch (PDOException $e) {
        echo $e->getMessage();
        echo "실패";
    }
/*
    $conn = mysqli_connect("13.209.50.185", "root", "cww1003", "choi");

    $insert_query = "INSERT INTO test1 (name) VALUES('한글')";

    mysqli_query($conn, $insert_query);

    mysqli_close($conn);*/

?>
