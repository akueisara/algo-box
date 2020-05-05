#include <algorithm>
#include <iostream>
#include <vector>
using std::vector;
using namespace std;
int count(vector<int> &a,int x,int left,int right){
    int count1=0;
    
    for(int i=left;i<=right;i++)
        if(a[i]==x)
            count1+=1;
    
    return count1;
}
    
  
int get_majority_element(vector<int> &a, int left, int right) {
  if (left == right) return a[left];
  //write your code here
  
  int mid = (left+right)/2;
  int l = get_majority_element(a,left,mid);
  int r = get_majority_element(a,mid+1,right);
  
  if(l==r)
    return l;
  
  int lint1=count(a,l,left,right);
  int rint1=count(a,r,left,right);
  
  return lint1>rint1?l:r;
}

int main() {
  int n,x,c;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  x= get_majority_element(a, 0, a.size()-1);
  c=count(a,x,0,a.size()-1);
  if(c>n/2)
    cout<<1<<"\n";
  else
    cout<<0<<"\n";
}
