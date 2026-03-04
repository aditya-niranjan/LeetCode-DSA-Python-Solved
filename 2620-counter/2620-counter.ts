function createCounter(n: number): () => number {
    let curr = n;

    return function():number {
        const result = curr;
        curr++;
        return result
    }
        
}


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */