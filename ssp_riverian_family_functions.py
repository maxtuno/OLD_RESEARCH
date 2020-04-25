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

# Very Old Wordk on Riverian Family Functions (LoL XD)
# This is a Riverian Function is a number tha in theit digits contains the sums of each subset on the list
# The original idea was that to search for a specific target you only had to look at the output of the function.
# It is theoretically interesting and is one of the beginnings of the NUMBER THEORY EQUATION OF SAT (http://independent.academia.edu/oarr)
# but is not practical.


def R(k, n, m):
    return (10**((2**k) * m)) * (10**((2**n) * m)) // ((10**((2**k) * m) + 1) * (10**m - 1))


S = [31, 554, 523, 5]
pad = 5

print(int(sum([R(k, len(S), pad) * S[k] for k in range(len(S))])))


def powerset(s):
    x = len(s)
    for i in range(1 << x):
        sub = [s[j] for j in range(x) if (i & (1 << j))]
        print(sum(sub), sub)


powerset(S)

"""
# python3 ssp_riverian_family_functions.py
1113010820055900528005900055900036000050110801077005540052300585005540003100000
0 []
31 [31]
554 [554]
585 [31, 554]
523 [523]
554 [31, 523]
1077 [554, 523]
1108 [31, 554, 523]
5 [5]
36 [31, 5]
559 [554, 5]
590 [31, 554, 5]
528 [523, 5]
559 [31, 523, 5]
1082 [554, 523, 5]
1113 [31, 554, 523, 5]
"""
