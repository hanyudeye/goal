<?php

class FormValidator{
    public static $regexes=Array(
        'date'=>"^[0-9]{4}[-/][0-9]{1,2}[-/][0-9]{1,2}\$"
    );

    public function __construct($validations=array(),)
    {
        
    }
}
