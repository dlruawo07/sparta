const users = ["Lee", "Kim", "Park", 2];

try {
  for (let user of users) {
    console.log(user.toUpperCase());
  }
} catch (e) {
  console.error(`Error: ${e.message}`);
}
