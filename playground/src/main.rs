// main.rs
// Solomon Himelbloom
// 2024-02-23
//
// For CS 601 Spring 2024

use llvm_ir::Module;

// https://mcyoung.xyz/2023/08/01/llvm-ir/#back-to-basic-blocks
pub fn square(x: i32) -> i32 {
    x * x
}

fn main() {
    let _module = Module::from_bc_path("source.bc");
    let version = llvm_ir::llvm_version();

    println!(">> LLVM {} -- Intermediate Representation (IR)", version);
}
