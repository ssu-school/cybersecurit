const primeNumber = 95971;

function modulo(a, m) {
  result = a % m;
  return result < 0 ? result + m : result;
}

function modInverse(a, m) {
  [a, m] = [Number(a), Number(m)];

  if (Number.isNaN(a) || Number.isNaN(m)) {
    return NaN;
  }

  a = ((a % m) + m) % m;
  if (!a || m < 2) {
    return NaN;
  }

  const s = [];
  let b = m;
  while (b) {
    [a, b] = [b, a % b];
    s.push({ a, b });
  }
  if (a !== 1) {
    return NaN;
  }

  let x = 1,
    y = 0;
  for (let i = s.length - 2; i >= 0; --i) {
    [x, y] = [y, x - y * Math.floor(s[i].a / s[i].b)];
  }
  return ((y % m) + m) % m;
}

function getRandomInt() {
  return Math.floor(Math.random() * (95971 + 1));
}

function IsExistX(shares, N, x) {
  for (let i = 0; i < N; i++) {
    if (shares[i][0] == x) {
      return true;
    }
  }

  return false;
}

function create(message, K, N) {
  const messageBuffer = new Buffer.from(message);
  const secrets = [...messageBuffer];
  const msgLength = secrets.length;
  const polynomials = new Array(msgLength);

  for (let i = 0; i < msgLength; i++) {
    polynomials[i] = new Array(K).fill(0);
    polynomials[i][0] = secrets[i];

    for (let j = 1; j < K; j++) {
      polynomials[i][j] = getRandomInt();
    }
  }

  const shares = new Array(msgLength);
  for (let i = 0; i < msgLength; i++) {
    shares[i] = new Array(N);
  }

  for (let i = 0; i < msgLength; i++) {
    for (let j = 0; j < N; j++) {
      shares[i][j] = new Array(2);
      do {
        x = getRandomInt();
      } while (IsExistX(shares[i], j, x));
      shares[i][j][0] = x;
      shares[i][j][1] = evaludatePolynomial(polynomials[i], x);
    }
  }

  const _shares = new Array(N);
  for (let i = 0; i < N; i++) {
    _shares[i] = new Array(msgLength);
    for (let j = 0; j < msgLength; j++) {
      _shares[i][j] = new Array(2);
    }
  }
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < msgLength; j++) {
      _shares[i][j][0] = shares[j][i][0];
      _shares[i][j][1] = shares[j][i][1];
    }
  }
  //   console.log(_shares);
  return _shares;
}

function evaludatePolynomial(polynomial, x) {
  const last = polynomial.length - 1;
  let result = polynomial[last];

  for (let i = last - 1; i >= 0; i--) {
    result = result * x;
    result = result + polynomial[i];
    result = modulo(result, primeNumber);
  }

  return result;
}

function combine(shares) {
  let secret = new Array(shares[0].length).fill(0);
  var buffer = new Buffer.alloc(shares[0].length);

  for (let k = 0; k < shares[0].length; k++) {
    for (let i = 0; i < shares.length; i++) {
      const share = shares[i][k];
      const x = share[0];
      const y = share[1];

      let numerator = 1;
      let denominator = 1;

      for (let j = 0; j < shares.length; j++) {
        if (i != j) {
          numerator = numerator * -shares[j][k][0];
          numerator = modulo(numerator, primeNumber);

          denominator = denominator * (x - shares[j][k][0]);
          denominator = modulo(denominator, primeNumber);
        }
      }
      inversed = modInverse(denominator, primeNumber);

      secret[k] = secret[k] + y * (numerator * inversed);
      secret[k] = modulo(secret[k], primeNumber);
    }
  }

  for (let i = 0; i < shares[0].length; i++) {
    buffer[i] = secret[i];
  }

  return buffer;
}

const shares = create("안녕하세요!!! !a sdjklfjs", 5, 10);
console.log(combine(shares.slice(1, 6)).toString("utf8"));
