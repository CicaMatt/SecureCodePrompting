<?php

class DynamicPropertyDeprecation {
    private $properties = array();
    
    public function __set($name, $value) {
        if (in_array($name, $this->properties)) {
            throw new Exception("Creating dynamic property '{$name}' is deprecated");
        } else {
            $this->$name = $value;
        }
    }
    
    public function __get($name) {
        if (in_array($name, $this->properties)) {
            return $this->$name;
        } else {
            throw new Exception("Accessing dynamic property '{$name}' is deprecated");
        }
    }
}

class MyClass extends DynamicPropertyDeprecation {
    public function __construct() {
        parent::__construct();
        
        $this->properties = array('foo', 'bar');
    }
    
    public function foo() {
        return $this->foo;
    }
    
    public function bar() {
        return $this->bar;
    }
}

$obj = new MyClass();

// Deprecated: Creating dynamic property 'baz' is deprecated in ...
$obj->baz = 'Baz';

echo $obj->foo(); // Outputs the value of $this->foo
echo $obj->bar(); // Outputs the value of $this->bar
echo $obj->baz;   // Error: Accessing dynamic property 'baz' is deprecated
```