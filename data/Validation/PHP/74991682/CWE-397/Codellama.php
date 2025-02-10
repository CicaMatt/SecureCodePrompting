<?php

// Use the new method signatures for Dynamic Properties
class MyClass {
    public function getProperty($name) {
        return $this->{$name};
    }
    
    public function setProperty($name, $value) {
        $this->{$name} = $value;
    }
}