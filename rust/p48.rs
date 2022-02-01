fn power_mod(n:u16, p:u16) -> u64 {
    let mut k:u64 = n as u64;
    for _ in 1..p {
        k *= n as u64;
        k %= 10_u64.pow(10);
    }
    return k;
}

fn main() {
    let mut sum: u64 = 0;
    for x in 1..1001 {
        sum += power_mod(x,x);
        sum %= 10_u64.pow(10);
    }
    println!("{}",sum)
}
