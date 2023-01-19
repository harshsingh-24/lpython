from ltypes import (i8, dataclass, i32, f32, c32, f64, i16, i64, c64,
    ccall, CPtr, c_p_pointer, Pointer)
from numpy import empty, int32

@dataclass
class buffer_struct:
    buffer8: i8
    buffer1: i32
    buffer2: f32
    buffer3: c32
    buffer4: f64
    buffer5: i16
    buffer6: i64
    buffer7: c64

@dataclass
class buffer_struct_array:
    buffer8: i8[100]
    buffer1: i32[32]
    buffer2: f32[32]
    buffer4: f64[32]
    buffer5: i16[64]
    buffer6: i64[16]
    buffer3: c32[16]
    buffer7: c64[8]

@ccall
def get_buffer() -> CPtr:
    pass

@ccall
def fill_buffer(buffer_cptr: CPtr):
    pass

@ccall
def get_buffer_array() -> CPtr:
    pass

@ccall
def fill_buffer_array(buffer_cptr: CPtr):
    pass

def f():
    b: CPtr = get_buffer()
    pb: Pointer[buffer_struct] = c_p_pointer(b, buffer_struct)
    pb.buffer8 = i8(3)
    pb.buffer1 = i32(4)
    pb.buffer2 = f32(5)
    pb.buffer3 = c32(9)
    pb.buffer4 = f64(6)
    pb.buffer5 = i16(7)
    pb.buffer6 = i64(8)
    pb.buffer7 = c64(10)
    print(pb.buffer8)
    print(pb.buffer1)
    print(pb.buffer2)
    print(pb.buffer3)
    print(pb.buffer4)
    print(pb.buffer5)
    print(pb.buffer6)
    print(pb.buffer7)
    assert pb.buffer8 == i8(3)
    assert pb.buffer1 == i32(4)
    assert pb.buffer2 == f32(5)
    assert pb.buffer3 == c32(9)
    assert pb.buffer4 == f64(6)
    assert pb.buffer5 == i16(7)
    assert pb.buffer6 == i64(8)
    assert pb.buffer7 == c64(10)

    fill_buffer(b)
    print(pb.buffer8)
    print(pb.buffer1)
    print(pb.buffer2)
    print(pb.buffer3)
    print(pb.buffer4)
    print(pb.buffer5)
    print(pb.buffer6)
    print(pb.buffer7)
    assert pb.buffer8 == i8(8)
    assert pb.buffer1 == i32(9)
    assert pb.buffer2 == f32(10)
    assert pb.buffer3 == c32(14) + c32(15j)
    assert pb.buffer4 == f64(11)
    assert pb.buffer5 == i16(12)
    assert pb.buffer6 == i64(13)
    assert pb.buffer7 == c64(16) + c64(17j)

def f_array():
    i: i32
    b: CPtr = get_buffer_array()
    pb: Pointer[buffer_struct_array] = c_p_pointer(b, buffer_struct_array)
    pb.buffer1 = empty(32, dtype=int32)
    print(pb.buffer1[15])

    fill_buffer_array(b)
    for i in range(100):
        print(pb.buffer8[i])
        assert pb.buffer8[i] == i8(i + 8)

    for i in range(32):
        print(pb.buffer1[i], pb.buffer2[i], pb.buffer4[i])
        assert pb.buffer1[i] == i32(i + 1)
        assert pb.buffer2[i] == f32(i + 2)
        assert pb.buffer4[i] == f64(i + 4)

    for i in range(64):
        print(pb.buffer5[i])
        assert pb.buffer5[i] == i16(i + 5)

    for i in range(16):
        print(pb.buffer6[i], pb.buffer3[i])
        assert pb.buffer6[i] == i64(i + 6)
        assert pb.buffer3[i] == c32(i + 3)

    for i in range(8):
        print(pb.buffer7[i])
        assert pb.buffer7[i] == c64(i + 7)


f()
f_array()
