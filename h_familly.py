"""
///////////////////////////////////////////////////////////////////////////////
//        Copyright (c) 2012-2020 Oscar Riveros. all rights reserved.        //
//                        oscar.riveros@peqnp.science                        //
//                                                                           //
//   without any restriction, Oscar Riveros reserved rights, patents and     //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# https://github.com/www-PEQNP-science/OLD_RESEARCH/blob/master/P_NP_The_Collapse_of_Hierarchies.pdf

def h(n):
    return (2 ** n) ** (2 ** n) + ((2 ** n) - (2 ** n) ** (2 ** n)) // (2 ** n - 1) ** 2


if __name__ == '__main__':
    print(bin(h(1))[2:])
    print(bin(h(2))[2:])
    print(bin(h(3))[2:])
    print(bin(h(4))[2:])

"""
10
11100100
111110101100011010001000
1111111011011100101110101001100001110110010101000011001000010000
"""