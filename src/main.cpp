#include <cmath>
#include <cstdio>
#include <cstdlib>
#include "buildconfig/BuildConfig.h"

#include "fspp/fuse/Fuse.h"
#include "fspp/impl/FilesystemImpl.h"
#include "copyfs/CopyDevice.h"
#include "cryfs_lib/CryDevice.h"
#include "blobstore/implementations/ondisk/OnDiskBlobStore.h"

namespace bf = boost::filesystem;

using blobstore::ondisk::OnDiskBlobStore;

using std::make_unique;

int main (int argc, char *argv[])
{
  printf("Version: %d\n", buildconfig::VERSION::MAJOR);
  auto blobStore = make_unique<OnDiskBlobStore>(bf::path("/home/heinzi/cryfstest/root"));
  auto config = make_unique<cryfs::CryConfig>(bf::path("/home/heinzi/cryfstest/config.json"));
  cryfs::CryDevice device(std::move(config), std::move(blobStore));
  fspp::FilesystemImpl fsimpl(&device);
  fspp::fuse::Fuse fuse(&fsimpl);
  fuse.run(argc, argv);
  return 0;
}
