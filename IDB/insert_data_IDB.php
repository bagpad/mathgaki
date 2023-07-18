<?php
    /* DB 연결 정보*/
    $host = "localhost";
    $user = "tkddn4508";
    $pw = "gom20726!";
    $dbName = "tkddn4508";
    $conn = mysqli_connect($host, $user, $pw, $dbName);
    $Completion = false;
    /* DB 연결 확인 */
    if($conn){ // 연결 성공
        /* DB SELECT*/
        $name = $_POST['name'];
        $student_name = $_POST['student_name'];
        $error_count = $_POST['error_count'];
        $MSG = $_POST['MSG']; 
        $MSG_TF = $_POST['MSG_TF'];

        $stmt = $conn->prepare("SELECT COUNT(*) AS count FROM math101 WHERE name = ? AND student_name = ?");
        $stmt->bind_param("ii", $name, $student_name);
        $stmt->execute();
        $result = $stmt->get_result();
        $row = mysqli_fetch_array($result);
        if ($row['count'] == 0) {
            $stmt = $conn->prepare("INSERT INTO math101 (name, student_name, error_count, MSG, MSG_TF) VALUES (?, ?, ?, ?, ?)");
            $stmt->bind_param("iiiiii", 
                $name, 
                $student_name, 
                $error_count, 
                $MSG, 
                $MSG_TF, 

            );
            if($stmt->execute()){
                $Completion = true;
                $idx = mysqli_insert_id($conn);
            }else{
                $Completion = false;
            }
        }
        if($Completion == true){
            $json = json_encode(array("result" => 'success', "msg" => 'success', "name" => $name, "student_name" => $student_name, "error_count" => $error_count, "MSG" => $MSG, "MSG_TF" => $MSG_TF,"idx" =>$idx));
        }else{
            $json = json_encode(array("result" => 'fail', "msg" => 'Completion fail'));
        }
        echo($json);
        mysqli_close($conn);
    }else{ // 연결 실패 
        $json = json_encode(array("result" => 'fail', "msg" => 'login fail'));
        echo($json);
    }
?>