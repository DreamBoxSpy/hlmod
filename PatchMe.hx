import haxe.io.Bytes;

class TestClass {
    public var test: Int = 5;

    public function new() {}
}

class PatchMe {
    static function main() {
        var val = get_value();
        var val2 = 2.0;
        thing(val, val2, "Unpatched message!", new TestClass());
    }

    static function get_value(): Float {
        return 1.0;
    }

    static function thing(val: Float, val2: Float, msg: String, val3: TestClass) {
        if (val == 2.0) {
            trace(msg);
            trace(val3.test);
        } else {
            trace("Patch failed!");
        }
    }
}