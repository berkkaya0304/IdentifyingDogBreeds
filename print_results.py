# Name: Berk Kaya
# Date: 20.06.2024
def print_results(results_dic, results_stats, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if user indicates
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index) idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image
                            and classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
      results_stats - Dictionary that contains the results statistics (either
                         a percentage or a count) where the key is the statistic's
                         name (starting with 'pct' for percentage or 'n' for count)
      model - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images, values must be
              either: resnet, alexnet, or vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and
                             False doesn't print anything(default) (bool)
      print_incorrect_breed - True prints incorrectly classified dog breeds and
                              False doesn't print anything(default) (bool)
    Returns:
           None - simply printing results.
    """
    # Print model architecture
    print(f"\n\n*** Results Summary for CNN Model Architecture {model.upper()} ***")

    # Print summary counts
    print(f"{'N Images':<20}: {results_stats['n_images']}")
    print(f"{'N Dog Images':<20}: {results_stats['n_dogs_img']}")
    print(f"{'N Not-Dog Images':<20}: {results_stats['n_notdogs_img']}")

    # Print summary statistics
    print(f"\n\n*** Results Statistics ***")
    for key in results_stats:
        if key.startswith('pct'):
            print(f"{key:<20}: {results_stats[key]:.2f}%")

    # Print incorrect classifications of dogs
    if print_incorrect_dogs:
        print("\n\n*** Incorrectly Classified Dogs ***")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print(f"Real: {results_dic[key][0]}  Classifier: {results_dic[key][1]}")

    # Print incorrect classifications of dog breeds
    if print_incorrect_breed:
        print("\n\n*** Incorrectly Classified Breeds ***")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print(f"Real: {results_dic[key][0]}  Classifier: {results_dic[key][1]}")
