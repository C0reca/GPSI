<link rel="stylesheet" type="text/css" href="style.css" media="screen" />
<h1>Dados a enviar</h1>
<form action="adicionar_action.php" method="POST">
<fieldset class="adicionar">
    <legend>Formulário</legend>
    <label>
        Número:<input type="text" name="numero" class="numero" size="5" >
    </label>
    <br><br>
    <label>
        Nome:<input type="text" name="name" class="name">
    </label>
    <br><br>
    <label>
        Morada:<input type="text" name="morada" class="morada" >
    </label>
    <br><br>
    <label>
        Idade:<input type="text" name="idade" class="idade" size="3" >
    </label>
    <br><br>
    <input type="submit" value="Enviar Dados">
    <input type="reset" value="Limpar Dados">
</fieldset>
</form>
