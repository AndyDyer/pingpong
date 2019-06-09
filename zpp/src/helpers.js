function deepCopy(obj) {
  return obj === undefined ? undefined : JSON.parse(JSON.stringify(obj));
}

export default {
  deepCopy,
};
