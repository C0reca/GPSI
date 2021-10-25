<?php
//PDO
$servername="localhost";
$username="root";
$password="";
$database="vendas";

//Criação de uma nova ligação
try{
    $conn=new PDO("mysql:host=$servername;dbname=$database",$username,$password);
    // Verificação da ligação
    $conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    //defenir o modo de erro PDO para exceção
    echo "ligação estabelecida";
}catch(PDOException $msg){
    echo "ocorreu um erro de ligação à base de dados:".$msg->getMessage();
}
?>
