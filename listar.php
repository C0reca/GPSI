<?php
require "config.php";
$lista=[];
$sql=$conn->query("select * from aluno");
if($sql->rowCount()>0){
    $lista=$sql->fetchAll(PDO::FETCH_ASSOC);
}
?>
<link rel="stylesheet" type="text/css" href="style.css" media="screen" />
<h1>Listar Registos</h1><br>
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
<?php echo "<br><a href='adicionar.php'>Voltar ao formulario de entrada</a>";?>