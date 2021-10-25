<?php
require "config.php";
$lista=[];
$name=filter_input(INPUT_POST,"nome");
$sql=$conn->query("SELECT * FROM `aluno` WHERE `nome` LIKE '%".$name."%'");
if($sql->rowCount()>0){
    $lista=$sql->fetchAll(PDO::FETCH_ASSOC);
}
?>

<h1>Listar Registos</h1><br>
<a>Nome Procurado: <?php echo $name;?></a><br><br>
<a>Nº de registos encontrados: <?php echo $sql->rowCount();?></a><br><br>
<table>
    <tr>
        <th>Número</th>
        <th>Nome</th>
        <th>Morada</th>
        <th>Idade</th>
    </tr>
    <?php foreach($lista as $utilizador):?>
        <tr>
            <td><?php echo $utilizador['numero'];?></td>
            <td><?php echo $utilizador['nome'];?></td>
            <td><?php echo $utilizador['morada'];?></td>
            <td><?php echo $utilizador['idade'];?></td>
        </tr>
    <?php endforeach; ?>
    
</table>
<br><a href='listar.php'>Listar registos</a>