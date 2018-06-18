var interiorColorMap = [];
var tmp = 1.0;
for (var i = 0; i < 256; ++i) {
    interiorColorMap.push(tmp);
    tmp *= 7 / 8;
}

function iterateEquation(Cr, Ci, iterations, Dr, Di) {
    var Zr = Cr;
    var Zi = Ci;
    var Tr = Cr * Cr;
    var Ti = Ci * Ci;
    var n = 0;
    var L = Math.min(Tr, Ti);

    for (; n < iterations && (Tr + Ti) <= 100; ++n) {
        Zi = 2 * Zr * Zi + Di;
        Zr = Tr - Ti + Dr;
        Tr = Zr * Zr;
        Ti = Zi * Zi;
        if (Tr < L) {
            L = Tr;
        }
        if (Ti < L) {
            L = Ti;
        }
    }

    /*
     * Fractal exterior, color using escape time
     */
    if (Tr + Ti > 100) {
        var v = n;
        var e = (Tr + Ti) / 100;
        if (e < 10) {
            v -= (e - 1) / 18;
        } else {
            v -= 0.5 + (e - 10) / 180;
        }
        v = v / iterations;
        v = 2 * v - v * v;
        v = 2 * v - v * v;
        return 255 - 255 * v;
    }

    /*
     * Fractal interior, color using Pickover stalk
     */
    var v = 0;
    var s = 128;
    while (s >= 1) {
        if (L < interiorColorMap[v + s]) {
            v += s;
        }
        s /= 2;
    }
    return v;
}

var data = new Uint8Array(640 * 480)

function draw(dr, di) {
    var steps = 256;
    var step = 3 / 512;

    var Dr = dr;
    var Di = di;
    var off = 0;


    for (sy = 0; sy < 480; ++sy) {
        var Ci = (sy + 0.5 - 240) * step;
        for (var sx = 0; sx < 640; ++sx) {
            var Cr = (sx + 0.5 - 320) * step;
            var v = 0;

            for (var sr = -1; sr <= 1; ++sr) {
                for (var si = -1; si <= 1; ++si) {
                    v += iterateEquation(Cr + sr * step / 4, Ci + si * step / 4, steps, Dr, Di);
                }
            }

            v = v / 9;
            var C = Math.round(v)
            data[off++] = C
        }
    }
    return data
}

var PNG = require('png-js');

function calc(p, acc, point) {
    //当前点为point，图像数据为p，精度为acc
    var less_val = 640 * 480 * 256 * 256
    var less_point = point//当前最优结果，与原图像差距最小的点
    var cnt = 0
    //平面图四分法求最优值，在以point为中心、边长为acc*4的正方形中尝试16个解，然后进一步缩小范围
    for (var r = point.r - (acc * 2); r <= (point.r + acc * 2); r = r + (acc / 4.0))
        for (var i = (point.i - (acc * 2)); i <= (point.i + acc * 2); i = i + (acc / 4.0)) {
            var rr = r, ii = i
            var d = draw(rr, ii)
            var diff = 0
            for (var x = 0; x < d.length; x++) {
                diff += (p[x * 4] - d[x]) * (p[x * 4] - d[x])
            }
            if (diff < less_val) {
                less_val = diff
                less_point = {r: rr, i: ii}
            }
            cnt = cnt + 1
        }
    return less_point
}

var img = "ailuj/0.png"

PNG.decode(img, function (p) {
    var point = {r: 0, i: 0}
    var acc = 1
    for (var i = 0; i < 100; i++) {
        point = calc(p, acc, point)
        acc = acc / 2
        console.log(point)
    }
    console.log(less_point)
})