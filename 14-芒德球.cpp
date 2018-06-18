#include <stdio.h>
#include <math.h>
struct vec {
    double x, y, z;
    vec(double r=0, double g=0, double b=0){ x=r; y=g; z=b; }
    vec operator+(const vec &b) const { return vec(x+b.x,y+b.y,z+b.z); }
    vec operator*(double b) const { return vec(x*b,y*b,z*b); }
    vec norm(){ return *this*(1/sqrt(x*x+y*y+z*z)); }
    vec operator%(vec&b){return vec(y*b.z-z*b.y,z*b.x-x*b.z,x*b.y-y*b.x);}
};
static vec map(vec p) {
    vec z=p, dz=vec(0.0, 0.0, 0.0);
    double power=8.0, r, tta, phi, dr=1.0, t0=1.0;
    for(int i=0;i<7;++i) {
        if((r=sqrt(z.x*z.x+z.y*z.y+z.z*z.z)) > 2.0) break;
        tta=acos(z.y/r)*power; phi=atan(z.z/z.x)*power;
 // spherical
        dr=pow(r, power-1.0)*dr*power+1.0;
// derevative
        r=pow(r, power);
        z=vec(sin(tta)*cos(phi), cos(tta), sin(tta)*sin(phi))*r+p;
        t0=t0<r?t0:r;
 // orbit trap, to mimic ao
    }
    return vec(0.5*log(r)*r/dr, t0, 0.0);
 // distance estimation
}
static vec trace(int x, int y){
 // ray marcher
    vec uv=vec((x*2.0/640.0-1.0)*640.0/480.0, y*2.0/480.0-1.0, 0.0);
    vec ro=vec(0.0, 2.0, 2.2), up=vec(0.0,1.0,0.0);
    vec cf=(ro*-1.0).norm(), cs=(cf%up).norm();
    vec rd=(cs*uv.x+(cs%cf).norm()*uv.y+cf*2.8).norm();
    vec p, col; double t=0.0;
    while(t<20.0) {
        p=ro+rd*t;
        vec akuma=map(p);
        if(akuma.x<0.0001) return vec(akuma.y, akuma.y, akuma.y);
        t+=akuma.x;
    }
    return vec(1.0, 1.0, 1.0);
}
int main() {
    FILE *f=fopen("image.ppm", "w");
    fprintf(f,"P3\n%d %d\n%d\n",640,480,255);
    for(int i=0;i<480;i++)
        for(int j=0;j<640;++j){
            vec col=trace(i, j)*255.0;
            fprintf(f,"%d %d %d ",int(col.x),int(col.y),int(col.z));
        }
    fclose(f);
    return 0;
}