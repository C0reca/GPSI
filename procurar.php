
<h1>Escreve o nome a procurar</h1><br>
<form action="procurar_action.php" method="POST">
    <label>
        Nome a procurar: <input type="text" name="nome">
    </label>
    <br><br>
    <input type="submit" value="Procurar registos">
</form>
<br><a href='adicionar.php'>Voltar à entrada</a><br><br>
<a href='listar.php'>Listar registos</a><br><br>

<form action="apagar_action.php" method="POST">
    <label>
        Nome a apagar: <input type="text" name="nome">
    </label>
    <br><br>
    <input type="submit" value="Apagar nome">
</form>
