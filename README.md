# OperaGX x Discord Nitro Promotion Generator

#### A collection of python scripts that generate a 1-month Discord Nitro promotion link from the ongoing promotion with Opera GX. All scripts are coded solely by me, but I may not be the first to code this.

## Generators
1. Basic Generator | This is the bare bones of all other generators. The slowest but most reliable.
2. Bulk Generator | Temporarily stores codes, then bulk adds them. Faster, but errors cause temporary storage to be lost.
3. Threaded Generator | generates many codes simultaneously. Significant jump in speed but uses up more computing power.
4. Async Generator | Optimized and cleaner version of the threaded gen. The fastest by far, but gets easily rate limited.

## Usage
- Download the files (duh)
- Make sure they are all in the same folder, they are correctly named, and that there are no duplicates
- Run the desired generator with the desired configurations
- The result will be added to the _nitro-promo-codes.txt_ text file

## Disclaimer and License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This code is licensed under MIT. The full license is included in the _LICENSE_ file.
