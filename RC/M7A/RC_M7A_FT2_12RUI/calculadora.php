<?php 

class Calculadora{

    public $num=0;

    public function soma($string){
        return $this->num+=$string;
    }
    public function subtrai($string){
        return $this->num-=$string;
    }
    public function multiplica($string){
        return $this->num*=$string;
    }
    public function divide($string){
        return $this->num/=$string;
    }
    public function clear(){
        return $this->num=0;
    }
    public function total(){
        return $this->num;
    }
}
?>
