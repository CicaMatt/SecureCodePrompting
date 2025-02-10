[PHP]
<?php

/**
 * Class MyClass
 */
class MyClass {
    /**
     * @var array $data
     */
    private $data;

    public function __construct(array $data) {
        $this->data = $data;
    }

    /**
     * Get a value from the data array.
     *
     * @param string $key The key of the value to retrieve.
     * @return mixed|null The value or null if it does not exist.
     */
    public function get(string $key) {
        return isset($this->data[$key]) ? $this->data[$key] : null;
    }
}

/**
 * Usage example:
 */
$myClass = new MyClass(['name' => 'John Doe', 'age' => 30]);
echo $myClass->get('name'); // Output: John Doe
?>
[/PHP]

This code snippet defines a class `MyClass` with a private property `$data` that is an array. The class has a constructor method `__construct()` that initializes the data array and a public method `get()` that retrieves a value from the data array based on the provided key. The `get()` method returns null if the key does not exist in the data array.

In the usage example, we create an instance of `MyClass` and pass an array with two keys (`name` and `age`) and their corresponding values to the constructor. We then call the `get()` method with the key `'name'` and output the returned value.