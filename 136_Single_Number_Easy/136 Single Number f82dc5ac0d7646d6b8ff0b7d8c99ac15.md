# 136. Single Number

Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**

```
Input: nums = [2,2,1]
Output: 1

```

**Example 2:**

```
Input: nums = [4,1,2,1,2]
Output: 4

```

**Example 3:**

```
Input: nums = [1]
Output: 1

```

**Constraints:**

- `1 <= nums.length <= 3 * 104`
- `3 * 104 <= nums[i] <= 3 * 104`
- Each element in the array appears twice except for one element which appears only once.

Solução:

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
```

Explicação:

O código define uma classe chamada **`Solution`** com um método **`singleNumber`**. Este método recebe uma lista de números **`nums`** como argumento e retorna um número inteiro.

Vamos entender o que está acontecendo dentro do método **`singleNumber`**:

1. **`a = 0`**: Aqui, uma variável **`a`** é inicializada com o valor zero. Essa variável será usada para armazenar o resultado.
2. **`for i in nums:`**: Essa é uma estrutura de loop **`for`** que itera sobre cada elemento **`i`** na lista **`nums`**.
3. **`a ^= i`**: O operador **`^=`** é o operador de atribuição combinada XOR. A operação **`a ^= i`** realiza a operação de XOR bit a bit entre **`a`** e **`i`** e atribui o resultado a **`a`**.
    
    O operador XOR (ou exclusivo) retorna **`1`** se os bits comparados forem diferentes e **`0`** se forem iguais. Portanto, **`a ^= i`** está realizando o XOR entre **`a`** e cada elemento **`i`** da lista **`nums`**.
    
    Essa operação de XOR é usada para cancelar as duplicatas. Se um número aparece duas vezes na lista, o XOR entre ele e ele mesmo resultará em **`0`**. No entanto, se um número aparece apenas uma vez, o XOR entre ele e **`0`** (valor inicial de **`a`**) resultará no próprio número.
    
4. **`return a`**: Após iterar por todos os elementos da lista **`nums`** e realizar as operações de XOR, o resultado final é retornado.

O resultado final de **`a`** será o número que aparece apenas uma vez na lista **`nums`**. Isso ocorre porque todos os números duplicados acabam se cancelando devido às propriedades do operador XOR, e o número que aparece apenas uma vez permanece sem cancelamento.

Por exemplo, considere a lista **`nums = [1, 2, 2, 3, 3]`**. Aplicando as etapas acima, temos:

1. Inicialmente, **`a`** é definido como **`0`**.
2. **`a ^= 1`** resulta em **`1`** (0 XOR 1 = 1).
3. **`a ^= 2`** resulta em **`3`** (1 XOR 2 = 3).
4. **`a ^= 2`** resulta em **`1`** (3 XOR 2 = 1).
5. **`a ^= 3`** resulta em **`2`** (1 XOR 3 = 2).
6. **`a ^= 3`** resulta em **`1`** (2 XOR 3 = 1).

Portanto, o código utiliza a propriedade do operador XOR para determinar o número que aparece apenas uma vez na lista **`nums`**.