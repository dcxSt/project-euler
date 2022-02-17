use num::integer::sqrt;
use std::iter::Iterator;

// this function will return true if n is prime, false otherwise
fn isprime(n: u16) -> bool {
    match n {
        1 => return false,
        2 | 3 => return true,
        _ => {
            if n % 2 == 0 {
                return false;
            }
            let sqrtn = sqrt(n) as u16;
            for k in (3..(sqrtn + 1)).step_by(2) {
                // println!("n={} k={} n%k={}", n, k, n % k);
                if n % k == 0 {
                    return false;
                }
            }
            return true;
        }
    }
}

// removes character from string if it's there
// assumes the char is in there
trait Rmchar {
    fn contains(&self, c: char) -> bool;
    fn rmchar(&mut self, c: char);
}

impl Rmchar for String {
    fn contains(&self, c: char) -> bool {
        let idx: Option<usize> = self.find(c);
        match idx {
            None => false,
            _ => true,
        }
    }

    // removes first instance of a char
    fn rmchar(&mut self, c: char) {
        let idx: Option<usize> = self.find(c);
        match idx {
            None => {
                panic!("{} is not a character in {}", c, self);
            }
            Some(n) => {
                self.replace_range(n..(n + 1), "");
            }
        }
    }
}

fn isperm(a: u16, b: u16, c: u16) -> bool {
    // assumes a, b and c have the same number of digits
    // returns true if the digits of a,b,c are all permutations of each other
    let ast: String = a.to_string();
    let mut bst: String = b.to_string();
    let mut cst: String = c.to_string();
    for ch in ast.chars() {
        if bst.contains(ch) && cst.contains(ch) {
            bst.rmchar(ch);
            cst.rmchar(ch);
        } else {
            return false;
        }
    }
    return true;
}

fn main() {
    // n is each possible starting number of the arithmetic sequence
    for n in (1001..10000).step_by(2) {
        if isprime(n) {
            for step in (2..((10000 - n) / 2)).step_by(2) {
                if isperm(n, n + step, n + 2 * step) && isprime(n + step) && isprime(n + 2 * step) {
                    println!("{} + {} + {}", n, n + step, n + 2 * step);
                }
            }
        }
    }
}

#[cfg(test)]
mod tests {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;

    #[test]
    fn test_isprime() {
        assert_eq!(true, isprime(5));
        assert_eq!(true, isprime(2));
        assert_eq!(true, isprime(3));
        assert_eq!(false, isprime(4));
        assert_eq!(false, isprime(1));
    }

    #[test]
    fn test_contains() {
        let word:String = String::from("promise1234");
        assert_eq!(true, word.contains('o'));
        assert_eq!(true, word.contains('p'));
        assert_eq!(true, word.contains('2'));
        assert_eq!(false, word.contains('z'));
        assert_eq!(false, word.contains('9'));
    }

    #[test]
    fn test_rmchar() {
        let mut word:String = String::from("premise1234");
        word.rmchar('3');
        assert_eq!(String::from("premise124") , word);
        word.rmchar('e');
        assert_eq!(String::from("prmise124") , word);
    }
}



