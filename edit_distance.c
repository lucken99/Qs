#define MATCH 0 /* enumerated type symbol for match */
#define INSERT 1 /* enumerated type symbol for insert*/
#define DELETE 2 /* enumerated type symbol for delete*/

#define MAXLEN 45


typedef struct {
int cost;
int parent;
} cell; /* cost of reaching this cell */
/* parent cell */
cell m[MAXLEN+1][MAXLEN+1]; /* dynamic programming table */

int match(char c, char d){
    if (c == d) return(0);
    else return(1);
}

int indel(char c){
    return(1);
} 

// int string_compare(char *s, char *t, int i, int j){
//  int k;   // counter
//  int opt[3];  // cost of the three options 
//  int lowest_cost;  // lowest cost

//  if (i == 0) return(j * indel(' '));
//  if (j == 0) return(i * indel(' '));

//  opt[MATCH] = string_compare(s, t, i-1, j-1) + match(s[i], t[j]);
//  opt[INSERT] = string_compare(s, t, i, j-1) + indel(t[j]);
//  opt[DELETE] = string_compare(s, t, i-1, j) + indel(s[i]);

//  lowest_cost = opt[MATCH];
//  for (k=INSERT; k<=DELETE; k++){
//      if (opt[k] < lowest_cost) lowest_cost = opt[k];
//  }

//  return (lowest_cost);
// }


row_init(int i)
{
m[0][i].cost = i;
if (i>0)
m[0][i].parent = INSERT;
else
m[0][i].parent = -1;
}



column_init(int i)
{
m[i][0].cost = i;
if (i>0)
m[i][0].parent = DELETE;
else
m[i][0].parent = -1;
}

goal_cell(char *s, char *t, int *i, int *j)
{
*i = strlen(s) - 1;
*j = strlen(t) - 1;
}

insert_out(char *t, int j)
{
printf("I");
}

delete_out(char *s, int i)
{
printf("D");
}

match_out(char *s, char *t,
int i, int j)
{
if (s[i]==t[j]) printf("M");
else printf("S");
}

reconstruct_path(char *s, char *t, int i, int j)
{
if (m[i][j].parent == -1) return;
if (m[i][j].parent == MATCH) {
reconstruct_path(s,t,i-1,j-1);
match_out(s, t, i, j);
return;
}
if (m[i][j].parent == INSERT) {
reconstruct_path(s,t,i,j-1);
insert_out(t,j);
return;
}
if (m[i][j].parent == DELETE) {
reconstruct_path(s,t,i-1,j);
delete_out(s,i);
return;
}
}

int string_compare(char *s, char *t)
{
int i,j,k;
/* counters */
int opt[3];
/* cost of the three options */
for (i=0; i<MAXLEN; i++) {
row_init(i);
column_init(i);
}
for (i=1; i<strlen(s); i++) {
for (j=1; j<strlen(t); j++) {
opt[MATCH] = m[i-1][j-1].cost + match(s[i],t[j]);
opt[INSERT] = m[i][j-1].cost + indel(t[j]);
opt[DELETE] = m[i-1][j].cost + indel(s[i]);
m[i][j].cost = opt[MATCH];
m[i][j].parent = MATCH;
for (k=INSERT; k<=DELETE; k++)
if (opt[k] < m[i][j].cost) {
m[i][j].cost = opt[k];
m[i][j].parent = k;
}
}
}
goal_cell(s,t,&i,&j);
return( m[i][j].cost );
}

main(){
   int a;
   a = string_compare("asdasdf", "asgdh");
   printf("%d\n", a );
   reconstruct_path("asdasdf", "asgdlh", 7, 6);
}