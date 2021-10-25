<?php
require "config.php";
$name=filter_input(INPUT_POST,"nome");
$sql=$conn->prepare("select * from aluno where nome like '".$name."'");
$sql->execute();

if($sql->rowCount()===1){
    $sql=$conn->prepare("delete from aluno where nome like '".$name."'");
    $sql->execute();
    echo "<a>Nome apagado: ".$name."</a><br><br>";
    echo "<a>Nº de registos apagados: ".$sql->rowCount()."</a><br><br>";

}
else{
    echo "<a>Nome Procurado: ".$name."</a><br><br>";
    echo "<a>Nº de registos encontrados: ".$sql->rowCount()."</a><br><br>";
    echo "Nenhum registo com esse nome";
}
?>
<br><a href='listar.php'>Listar registos</a>