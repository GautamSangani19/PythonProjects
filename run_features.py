import os
import subprocess
import shutil
# Clean previous Allure results
if os.path.exists("allure-results"):
    for item in os.listdir("allure-results"):
        item_path = os.path.join("allure-results", item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
else:
    os.makedirs("allure-results")

# Define feature file batches
feature_batches = [
    [
        "features/login.feature",
        "features/profile_setup.feature",
        "features/Edit_profile.feature"
    ],
    [
        "features/post_job.feature",
        "features/draft_job.feature",
        "features/edit_job.feature",
        "features/search_functionality.feature"
    ],
    [
        "features/Add_Machinery.feature",
        "features/Filter.feature",
        "features/Machine_Like.feature"
    ],
    [
        "features/coin.feature",
        "features/Coin_history.feature",
        "features/payment_history.feature"
    ],
    [
        "features/refer_earn.feature",
        "features/settings.feature",
        "features/support.feature",
        "features/logout.feature",
        "features/Delete_account.feature"
    ]
]

# Run each batch
for batch in feature_batches:
    command = [
        "behave",
        *batch,
        "-f", "allure_behave.formatter:AllureFormatter",
        "-o", "allure-results",
        "--no-capture",
        "--no-capture-stderr"
    ]
    print(f"\n▶️ Running batch: {', '.join(batch)}")
    subprocess.run(command)

# Generate Allure Report
print("\n📊 Generating Allure Report...")
subprocess.run([r"C:\allure-2.34.0\bin\allure.bat", "serve", "allure-results"])
