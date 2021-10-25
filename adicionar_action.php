<h1>Inserir Registos</h1>
<?php
require "config.php";

$numero=filter_input(INPUT_POST,"numero");
$name=filter_input(INPUT_POST,"name");
$morada=filter_input(INPUT_POST,"morada");
$idade=filter_input(INPUT_POST,"idade");


if($numero && $name && $morada && $idade){

    $sql=$conn->prepare("select * from aluno where numero=:numero");
    $sql->bindValue(':numero',$numero);
    $sql->execute();
    if($sql->rowCount()===0){
        $sql=$conn->prepare("INSERT INTO aluno (numero,nome,morada,idade) VALUES (:numero,:name,:morada, :idade)");
        $sql->bindValue(':numero',$numero);
        $sql->bindValue(':name',$name);
        $sql->bindValue(':morada',$morada);
        $sql->bindValue(':idade',$idade);
        $sql->execute();

        echo "Dados recebidos:"."<br>";
        echo "Número: ".$numero."<br>";
        echo "Nome: ".$name."<br>";
        echo "Morada: ".$morada."<br>";
        echo "Idade: ".$idade."<br>"."<br>";
        echo "Dados inseridos"."<br>";
        echo "<a href='adicionar.php'>Voltar a entrada</a>"."<br>"."<br>";
        echo "<a href='listar.php'>Listar registos</a>";
        exit;
    }
    elseif($sql->rowCount()===1){
        echo "Número de aluno ja existente"."<br>";
        echo "<a href='adicionar.php'>Voltar a entrada</a>";
    }
    else{
        echo "Campos em falta. Volte atrás e tente de novo"."<br>";
        echo "<a href='adicionar.php'>Voltar a entrada</a>";
        exit;}
}
else{
    header("Location: adicionar.php");
    exit;
}
?> 
