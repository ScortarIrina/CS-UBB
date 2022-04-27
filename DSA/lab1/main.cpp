/*
Implement  in  C++  the  given container (ADT)  using  a given  representation  and  a dynamic  arrayas a data structure. 
You are not allowed to use the vector from STL or from any other library.

Obs:
    - Since your implementationwill use dynamic allocation, it is a good practice to implement a destructor,  
      copy  constructor  and  assignment  operator  as  well  (even  if  they  are  not  on  the interface).
    
    - You are not allowed to use  the functionsmemcpyand realloc, becauseit is not safe to use memcpy and realloc on memory  
      that  was  allocated with new. Also, if the memory location contains objects, undefined  behavior  can  occur. 
      The implementation  might  still  work  with these functions, but it is not a good practice to use them.
      
    - If you need auxiliary functions, fell free  to add them to the interface of the ADT,  but  make them private.


11) ADT Set – represented as a dynamic array of Boolean values.
    For example the set {5, 1, -4, 0, 8} can be represented as an array of 13 elements where 
    position 0 corresponds to element -4,  position  1  corresponds  to  element -3, ..., 
    position  12  corresponds  to  element  8:  
    [true, false, false, false, true, true, false, false, false, true, false, false, true].
*/

#include <iostream>
#include "Set.h"
#include "SetIterator.h"
#include "ShortTest.h"
#include "ExtendedTest.h"

using namespace std;

int main()
{
    testAll();
    testAllExtended();

    cout << "That's all!" << endl;

    return 0;
}
