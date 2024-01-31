async function getAllCupcakes() {
  try {
    const res = await axios.get("http://localhost:5000/api/cupcakes");
    return res.data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

cupcakeOutline =
  '<div> \
<table> \
    <tr> \
        <td> \
            <img class="image" src="https://tinyurl.com/demo-cupcake" height="75px"></img> \
        </td> \
        <td> \
            <table> \
                <tr><td class="flavor"> Vanilla </td></tr> \
                <tr> <td class="size"> medium size </td> </tr> \
                <tr> <td class="rating"> Rating: 9 </td> </tr> \
            </table> \
        </td> \
    </tr> \
</table> \
</div>';

function addCupcakeToPage(cupcake) {
  div = $(cupcakeOutline);
  div.find(".flavor").html("<strong>" + cupcake["flavor"] + "</strong>");
  div.find(".size").text(cupcake["size"] + " size");
  div.find(".rating").text("Rating:" + cupcake["rating"]);
  div.find(".image").attr("src", cupcake["image"]);
  $(".cupcake-list").append(div);
}

function addAllCupcakesToPage(cupcakes) {
  for (cupcake of cupcakes) {
    addCupcakeToPage(cupcake);
  }
}

async function showAllCupcakes() {
  const allCupcakes = await getAllCupcakes();
  addAllCupcakesToPage(allCupcakes["cupcakes"]);
}

showAllCupcakes();

////////////////////////////////////////////////////////////////////

async function postNewCupcake(cupcakeInfo) {
  //   console.log("posting", cupcakeInfo);
  try {
    const res = await axios.post(
      "http://localhost:5000/api/cupcakes",
      cupcakeInfo,
      { headers: { "Content-Type": "application/json" } }
    );
    return res;
  } catch (error) {
    console.log(error);
    return null;
  }
}

async function clickSubmit() {
  cupcakeInfo = {
    flavor: $("#flavor").val(),
    size: $("#size").val(),
    rating: $("#rating").val(),
  };
  if ($("#image").val() != "") {
    cupcakeInfo.image = $("#image").val();
  }
  res = await postNewCupcake(cupcakeInfo);
  addCupcakeToPage(res.data["cupcake"]);
  $("#flavor").val("");
  $("#size").val("");
  $("#rating").val("");
  $("#image").val("");
  //   console.log(res);
}

$("button").click(clickSubmit);
